<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LeetCode Practice</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      background-color: #f4f7fb;
      margin: 0;
      padding: 0;
    }
    header {
      background: linear-gradient(45deg, #ff7e5f, #feb47b);
      color: #fff;
      padding: 40px;
      text-align: center;
    }
    header h1 {
      font-size: 3rem;
      margin: 0;
    }
    .section {
      padding: 40px;
      text-align: center;
    }
    .section h2 {
      font-size: 2rem;
      color: #333;
    }
    .skills, .challenges {
      display: flex;
      justify-content: space-around;
      flex-wrap: wrap;
      margin-top: 20px;
    }
    .skill, .challenge {
      background-color: #fff;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
      margin: 10px;
      width: 280px;
      transition: transform 0.3s ease;
    }
    .skill:hover, .challenge:hover {
      transform: translateY(-10px);
    }
    .skill h3, .challenge h3 {
      margin: 0;
      color: #333;
      font-size: 1.5rem;
    }
    .skill p, .challenge p {
      font-size: 1.1rem;
      color: #555;
    }
    .cta {
      background-color: #ff7e5f;
      color: white;
      padding: 20px;
      text-align: center;
      font-size: 1.2rem;
      margin-top: 40px;
    }
    .cta a {
      color: white;
      text-decoration: none;
      font-weight: bold;
      padding: 10px 20px;
      background-color: #333;
      border-radius: 5px;
      transition: background-color 0.3s ease;
    }
    .cta a:hover {
      background-color: #ff6f61;
    }
    footer {
      background-color: #333;
      color: white;
      padding: 10px;
      text-align: center;
    }
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <h1>LeetCode Practice Repo</h1>
    <p>Level up your coding skills by solving algorithmic challenges!</p>
  </header>

  <!-- Introduction Section -->
  <section class="section">
    <h2>Welcome to my LeetCode Practice Repository!</h2>
    <p>Here I am solving various problems on LeetCode to improve my problem-solving and coding abilities. Explore the repository for my solutions and progress!</p>
  </section>

  <!-- Skills Section -->
  <section class="section skills">
    <h2>Skills I'm Improving</h2>
    <div class="skill">
      <h3>Data Structures</h3>
      <p>Arrays, Linked Lists, Trees, Graphs, Heaps, Stacks, and Queues</p>
    </div>
    <div class="skill">
      <h3>Algorithms</h3>
      <p>Sorting, Searching, Dynamic Programming, Backtracking, Greedy</p>
    </div>
    <div class="skill">
      <h3>Math & Geometry</h3>
      <p>Combinatorics, Number Theory, Bit Manipulation, Geometry</p>
    </div>
  </section>

  <!-- Challenges Section -->
  <section class="section challenges">
    <h2>Challenges Solved</h2>
    <div class="challenge">
      <h3>Easy Challenges</h3>
      <p>Learn the fundamentals of algorithms and data structures with easy LeetCode problems!</p>
    </div>
    <div class="challenge">
      <h3>Medium Challenges</h3>
      <p>Sharpen your skills with medium-level problems that require deeper insights!</p>
    </div>
    <div class="challenge">
      <h3>Hard Challenges</h3>
      <p>Push your limits and solve hard problems that require advanced techniques!</p>
    </div>
  </section>

  <!-- Call to Action -->
  <section class="cta">
    <p>Want to join me in this coding journey?</p>
    <a href="https://leetcode.com" target="_blank">Start Solving on LeetCode</a>
  </section>

  <!-- Footer -->
  <footer>
    <p>Happy Coding! 🧑‍💻</p>
  </footer>

</body>
</html>
