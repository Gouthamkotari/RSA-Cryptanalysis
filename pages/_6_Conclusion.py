from flask import render_template_string

def register(app):
    # FIX: Change the route from '/procedure' to '/conclusion'
    @app.route('/conclusion')
    def conclusion():
        html = '''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Conclusion</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
              body { background-color: #f4f7f6; }
              .card {
                border: none;
                border-radius: 0.75rem;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
              }
              .card:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 18px rgba(0, 0, 0, 0.12);
              }
              .btn { transition: all 0.3s ease; border-radius: 0.5rem; font-weight: 500; }
              .btn-primary { background-color: #007bff; border-color: #007bff; }
              .btn-primary:hover { background-color: #0056b3; border-color: #0056b3; transform: translateY(-1px); }
              .btn-secondary { background-color: #6c757d; border-color: #6c757d; }
              .btn-secondary:hover { background-color: #5a6268; border-color: #5a6268; }
              .card-title { font-weight: 600; color: #333; padding-bottom: 0.5rem; border-bottom: 1px solid #eee; margin-bottom: 1.5rem; }
            </style>
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
                  <h2 class="card-title">Conclusion</h2>
                  <p>This demonstration confirms that RSA keys where one prime factor is intentionally or accidentally small are highly vulnerable to simple factoring attacks like trial division.</p>
                  <p>To ensure security, always generate RSA primes of appropriate, large sizes (e.g., 1024-bit primes for a 2048-bit modulus) using cryptographically secure libraries that enforce proper key generation parameters.</p>
                  <a class="btn btn-secondary mt-3" href="/">Back to Home</a>
                </div>
              </div>
            </main>
          </body>
        </html>
        '''
        return render_template_string(html)