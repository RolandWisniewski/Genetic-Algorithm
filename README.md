# Genetic Algorithm for Image Approximation

This project implements a genetic algorithm to approximate a grayscale image using pixel-level evolution. The algorithm begins with a population of random images and iteratively evolves them to match a target image. The final output is a visual representation of the best individual's fitness progression and the generated image.

### Features

* Works with grayscale images of any resolution.
* Supports customizable population size, mutation rate, and maximum generations.
* Includes adaptive mutation rate to handle stagnation in fitness.
* Visualizes fitness progression and the best individual's evolution.
* Handles Ctrl+C gracefully, allowing you to interrupt and still view the fitness progress plot.

## How It Works

1. Initialization:
  - A target image is loaded and converted to grayscale.
  - The population is initialized with random pixel values (0–255).
2. Fitness Calculation:
  - Fitness is calculated as the sum of absolute differences between the target and candidate image.
3. Selection:
  - The top 50% of the population is selected for breeding.
4. Crossover:
  - Parents are combined using a mask-based crossover, producing offspring by mixing pixel regions.
5. Mutation:
  - Small random noise is added to some pixels, simulating mutations. Values are clamped between 0 and 255.
6. Replacement:
  - The population is replaced with the best individuals from the offspring and current population, ensuring elitism.
7. Termination:
  - The algorithm stops when the fitness reaches 0 or after the maximum number of generations is reached.

## Requirements

* Python 3.6 or higher
* Required Libraries:
  * `numpy`
  * `opencv-python`
  * `matplotlib`
You can install the dependencies using pip:
```bash
pip install numpy opencv-python matplotlib
```

## Usage

Run the program with default parameters:
```bash
python main.py
```
You can customize parameters directly in the script or modify the function call in the `main` function:

* `loc`: Path to the target image (default: `dog.jpg`).
* `POP_SIZE`: Population size (default: `1000`).
* `MUT_RATE`: Mutation rate (default: `0.01`).
* `MAX_GENERATION`: Maximum number of generations (default: `1000`).
Example:
```python
main(loc='path/to/image.png', POP_SIZE=500, MUT_RATE=0.05, MAX_GENERATION=2000)
```

## Program Flow

1. Start the program. A target image (`dog.jpg` by default) is loaded.
2. The algorithm begins evolving a population to approximate the target image.
3. Progress is displayed in the console:
  - Current generation
  - Best fitness
  - Total elapsed time
  - Progress bar
4. The best individual's progress is plotted every 100 generations.
5. Upon completion (or interruption with `Ctrl+C`), the fitness history is plotted, showing how fitness improved over generations.

## Example Output

### Progress Display:
```
Generation: 100
Fitness: 4321
Total time: 15.203 [s]
|❚❚❚❚❚❚❚❚❚❚          | 50.0%

Press Ctrl+C to force exit.
```
### Generated Image:
The algorithm displays the best individual for the final generation.

![Figure1](https://github.com/user-attachments/assets/d931bb39-3b06-464b-8bfe-b2154e4554fe)
### Fitness Progress Plot:
![Figure2](https://github.com/user-attachments/assets/d08987b5-9287-4fea-b7c4-d54943abcef6)

## Known Limitations

* High resolution images may require significant computational time due to the large population and pixel-by-pixel comparisons.
* The mutation rate must be carefully tuned to balance exploration and convergence.

## Inspiration, code snippets, etc.

* [Medium](https://medium.com/@Data_Aficionado_1083/genetic-algorithms-optimizing-success-through-evolutionary-computing-f4e7d452084f)

## Contribution

Contributions are welcome! If you have ideas for optimization or new features, feel free to fork the repository and submit a pull request.

## Author

Roland Wiśniewski\
GitHub: [RolandWisniewski](https://github.com/RolandWisniewski)
