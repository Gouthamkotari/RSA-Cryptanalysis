from flask import request, render_template_string
from math import isqrt

def parse_int(s):
    s = (s or '').strip()
    if not s:
        return None
    try:
        if s.lower().startswith('0x'):
            return int(s, 16)
        return int(s, 10)
    except ValueError:
        return None

def trial_division_small_factor(n, limit=None):
    if n % 2 == 0:
        return 2
    max_default = 1_000_000
    if limit is None:
        limit = min(max_default, isqrt(n))
    else:
        limit = min(limit, isqrt(n))
    i = 3
    while i <= limit:
        if n % i == 0:
            return i
        i += 2
    return None

def register(app):
    @app.route('/simulation', methods=['GET', 'POST'])
    def simulation():
        template = '''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Simulation</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
          </head>
          <body class="bg-light">
            <nav class="navbar navbar-dark bg-dark">
              <div class="container">
                <a class="navbar-brand" href="/">RSA Small-Factor Attack</a>
                <div>
                  <a class="btn btn-outline-light btn-sm" href="/">Home</a>
                </div>
              </div>
            </nav>
            <main class="container py-5">
              <div class="row">
                <div class="col-lg-6">
                  <div class="card mb-4 shadow-sm">
                    <div class="card-body">
                      <h5 class="card-title">Run Simulation</h5>
                      <form method="post">
                        <div class="mb-3">
                          <label class="form-label">Modulus n (decimal or 0xHEX)</label>
                          <input class="form-control" name="n" placeholder="e.g. 11413 or 0x2C65">
                        </div>
                        <div class="mb-3">
                          <label class="form-label">Public exponent e</label>
                          <input class="form-control" name="e" value="65537">
                        </div>
                        <div class="mb-3">
                          <label class="form-label">Ciphertext c (optional)</label>
                          <input class="form-control" name="c" placeholder="optional integer (decimal or 0xHEX)">
                        </div>
                        <div class="mb-3">
                          <label class="form-label">Max factor search limit (optional)</label>
                          <input class="form-control" name="limit" placeholder="e.g. 1000000">
                          <div class="form-text">Leave empty to use default (1,000,000 or sqrt(n) whichever is smaller).</div>
                        </div>
                        <button class="btn btn-primary" type="submit">Run Attack</button>
                      </form>
                    </div>
                  </div>
                  <div class="card shadow-sm">
                    <div class="card-body">
                      <h6>Quick test values</h6>
                      <p class="small mb-1"><strong>Example:</strong> n = 11413, e = 65537, c = 4901 (plaintext m=42)</p>
                      <p class="small">Use the helper script to generate more small RSA test vectors.</p>
                    </div>
                  </div>
                </div>

                <div class="col-lg-6">
                  {% if error %}
                  <div class="alert alert-danger">{{ error }}</div>
                  {% endif %}

                  {% if result %}
                  <div class="card shadow-sm mb-3">
                    <div class="card-body">
                      <h5 class="card-title">Result</h5>
                      {{ result|safe }}
                    </div>
                  </div>
                  {% else %}
                  <div class="card shadow-sm">
                    <div class="card-body">
                      <h5 class="card-title text-muted">Results will appear here</h5>
                      <p class="text-muted">Run the simulation with values on the left to see formatted results.</p>
                    </div>
                  </div>
                  {% endif %}
                </div>
              </div>

              <a class="btn btn-link mt-4" href="/">Back</a>
            </main>
          </body>
        </html>
        '''

        if request.method == 'GET':
            return render_template_string(template, result=None, error=None)

        # POST: process inputs
        n = parse_int(request.form.get('n', ''))
        e = parse_int(request.form.get('e', '65537')) or 65537
        c = parse_int(request.form.get('c', '')) if request.form.get('c', '').strip() else None
        limit_raw = request.form.get('limit', '').strip()
        limit = None
        if limit_raw:
            try:
                limit = int(limit_raw)
            except:
                limit = None

        if not n:
            return render_template_string(template, result=None, error="Please provide a valid modulus n.")

        p = trial_division_small_factor(n, limit)
        if not p:
            msg = f'<div class="alert alert-warning">No small factor found up to the search limit. Try increasing the limit or supply a smaller-n test value.</div>'
            msg += f'<pre class="mt-2">n = {n}</pre>'
            return render_template_string(template, result=msg, error=None)

        q = n // p
        phi = (p - 1) * (q - 1)
        try:
            d = pow(e, -1, phi)
        except ValueError:
            msg = f'<h6>Found factor p = {p}</h6>'
            msg += f'<div class="alert alert-danger">e and φ(n) are not coprime — modular inverse does not exist.</div>'
            msg += f'<pre>p = {p}\\nq = {q}\\nphi = {phi}</pre>'
            return render_template_string(template, result=msg, error=None)

        # Build result html
        res = '<div class="table-responsive"><table class="table table-sm table-bordered"><tbody>'
        res += f'<tr><th>n</th><td>{n}</td></tr>'
        res += f'<tr><th>p</th><td>{p}</td></tr>'
        res += f'<tr><th>q</th><td>{q}</td></tr>'
        res += f'<tr><th>e</th><td>{e}</td></tr>'
        res += f'<tr><th>d</th><td>{d}</td></tr>'
        res += '</tbody></table></div>'

        if c is not None:
            m = pow(c, d, n)
            res += '<h6>Decryption</h6>'
            res += '<pre class="small">ciphertext (int) = {}</pre>'.format(c)
            res += '<pre class="small">plaintext (int) = {}</pre>'.format(m)
            # try to show bytes / utf-8
            try:
                byte_len = (m.bit_length() + 7) // 8
                m_bytes = m.to_bytes(byte_len, 'big')
                stripped = m_bytes.lstrip(b'\\x00')
                decoded = None
                try:
                    decoded = stripped.decode('utf-8')
                except:
                    decoded = None
                res += '<pre class="small">plaintext (bytes) = {}</pre>'.format(m_bytes)
                res += '<pre class="small">plaintext (utf-8 if valid) = {}</pre>'.format(decoded)
            except Exception:
                pass

        return render_template_string(template, result=res, error=None)
