from flask import Flask
import pages._1_Introduction as intro
import pages._2_Objective as objective
import pages._3_Theory as theory
import pages._4_Simulation as sim
import pages._5_Procedure as proc
import pages._6_Conclusion as concl

app = Flask(__name__)

intro.register(app)
objective.register(app)
theory.register(app)
sim.register(app)
proc.register(app)
concl.register(app)

@app.route('/')
def index():
    return '''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>RSA Small-Factorization Demo</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
          /* General body background refinement */
          body {
            background-color: #f4f7f6; /* Lighter, less stark background */
          }
          
          /* Enhancing the main content cards for a professional look */
          .card {
            border: none;
            border-radius: 0.75rem; /* Smoother, larger border radius */
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); /* More subtle, deeper shadow */
            transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth transition */
          }
          
          /* Subtle lift effect on hover for cards (good for interactive elements) */
          .card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.12);
          }
          
          /* Enhancing buttons for smoother interaction */
          .btn {
            transition: all 0.3s ease;
            border-radius: 0.5rem;
            font-weight: 500;
          }
          /* Customizing the main primary button */
          .btn-primary {
            background-color: #007bff;
            border-color: #007bff;
          }
          .btn-primary:hover {
            background-color: #0056b3;
            border-color: #0056b3;
            transform: translateY(-1px);
          }
          /* Customizing secondary button */
          .btn-secondary {
            background-color: #6c757d;
            border-color: #6c757d;
          }
          .btn-secondary:hover {
            background-color: #5a6268;
            border-color: #5a6268;
          }

          /* Typography refinement in cards */
          .card-title {
            font-weight: 600;
            color: #333;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #eee;
            margin-bottom: 1.5rem;
          }

          /* Navigation link hover effect */
          .navbar-nav .nav-link {
              transition: color 0.3s ease;
          }
          .navbar-nav .nav-link:hover {
              color: #007bff !important;
          }
          
          /* Style for pre blocks (code/results) */
          pre {
            background-color: #f8f9fa; /* Light background for code */
            border: 1px solid #dee2e6;
            padding: 1rem;
            border-radius: 0.5rem;
            overflow-x: auto;
            color: #333;
            font-size: 0.9rem;
          }
        </style>
      </head>
      <body class="bg-light">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
          <div class="container">
            <a class="navbar-brand" href="/">RSA Small-Factor Attack</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav ms-auto">
                <li class="nav-item"><a class="nav-link" href="/introduction">Introduction</a></li>
                <li class="nav-item"><a class="nav-link" href="/objective">Objective</a></li>
                <li class="nav-item"><a class="nav-link" href="/theory">Theory</a></li>
                <li class="nav-item"><a class="nav-link" href="/simulation">Simulation</a></li>
                <li class="nav-item"><a class="nav-link" href="/procedure">Procedure</a></li>
                <li class="nav-item"><a class="nav-link" href="/conclusion">Conclusion</a></li>
              </ul>
            </div>
          </div>
        </nav>

        <main class="container py-5">
          <div class="card shadow-sm">
            <div class="card-body">
              <h1 class="card-title">RSA Cryptanalysis — Small-Factorization Attack</h1>
              <p class="lead">Demonstrates how a small prime factor of the modulus (n) can be quickly found to recover the private key and decrypt a ciphertext.</p>
              <hr>
              <p>Explore the theory behind the attack, follow the step-by-step procedure, or jump straight into the <a href="/simulation">Simulation</a> page to try custom values.</p>
              <div class="mt-4">
                <a class="btn btn-primary btn-lg me-3" href="/simulation">Start Simulation</a>
                <a class="btn btn-outline-secondary btn-lg" href="/theory">Learn The Theory</a>
              </div>
            </div>
          </div>
        </main>

        <footer class="text-center py-4 text-muted small">
          A security demonstration project.
        </footer>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
      </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)