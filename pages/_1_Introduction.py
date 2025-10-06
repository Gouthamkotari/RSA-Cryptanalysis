from flask import render_template_string

def register(app):
    @app.route('/introduction')
    def introduction():
        html = '''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Introduction</title>
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
                  <h2 class="card-title">Introduction</h2>
                  <p>RSA Cryptanalysis using a small-factorization attack is a method of breaking the RSA encryption scheme by exploiting cases where the RSA modulus (N) is the product of two primes (p) and (q), and one of these primes is unusually small. By efficiently factoring (N) using methods such as trial division or Pollard’s (p-1) algorithm, the attacker can recover the private key (d) from the public key (e) and modulus (N), allowing decryption of messages without authorization. This attack highlights the importance of choosing sufficiently large and balanced prime numbers in RSA key generation to maintain cryptographic security.</p>
                  <br>
                  <h4>About the experiment: </h4>
                  <p>This experiment demonstrates RSA cryptanalysis using a small‑factorization attack: you implement a program that, given an RSA public key (modulus (N) and public exponent (e)) and a ciphertext or sample RSA modulus, attempts to factor (N) when one factor is unusually small compared to the other. The single‑paragraph goal is to show how an attacker can exploit imbalanced key generation (e.g., a tiny prime factor (p)) by using straightforward factor‑search methods (trial division, Pollard’s p−1, or optimized trial up to a bound) to recover (p) and (q), compute the private exponent (d), and decrypt ciphertexts—thus illustrating both the implementation steps (input of (N,e), factoring routine, modular inverse computation, decryption) and the security lesson: securely generated RSA keys must avoid weak parameters (small/related primes) because they make keys trivially breakable and compromise confidentiality.</p>
                  <a class="btn btn-secondary mt-3" href="/">Back to Home</a>
                </div>
              </div>
            </main>
          </body>
        </html>
        '''
        return render_template_string(html)