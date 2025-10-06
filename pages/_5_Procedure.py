from flask import render_template_string

def register(app):
    @app.route('/procedure')
    def procedure():
        html = '''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Procedure</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
          </head>
          <body class="bg-light">
            <nav class="navbar navbar-dark bg-dark">
              <div class="container">
                <a class="navbar-brand" href="/">RSA Small-Factor Attack</a>
                <div>
                  <a class="btn btn-outline-light btn-sm" href="/simulation">Simulation</a>
                </div>
              </div>
            </nav>
            <main class="container py-5">
              <div class="card shadow-sm">
                <div class="card-body">
                  <h2>Procedure</h2>
                  <ol>
                    <li>Input the RSA modulus <code>n</code>, public exponent <code>e</code>, and optionally ciphertext <code>c</code>.</li>
                    <li>Attempt trial division to find a small factor <code>p</code> of <code>n</code>.</li>
                    <li>Compute <code>q = n / p</code>, <code>φ(n) = (p-1)(q-1)</code>, and <code>d = e⁻¹ mod φ(n)</code>.</li>
                    <li>Decrypt with <code>m = cᵈ mod n</code> if ciphertext provided.</li>
                  </ol>
                  <a class="btn btn-secondary mt-3" href="/">Back</a>
                </div>
              </div>
            </main>
          </body>
        </html>
        '''
        return render_template_string(html)
