# A Survey on Spiking Neural Networks (SNNs)

A comprehensive, community-oriented survey of Spiking Neural Networks — covering
neuron models, encoding schemes, training methods, neuromorphic hardware, and
applications. Written in LaTeX.

## 📄 Contents

The survey is organized into the following sections:

1. **Introduction** — motivation and scope
2. **Background** — from ANNs to SNNs, neural coding schemes
3. **Neuron Models** — LIF, Izhikevich, Hodgkin–Huxley, SRM, …
4. **Training Methods** — ANN-to-SNN conversion, surrogate gradients, STDP
5. **Neuromorphic Hardware** — TrueNorth, Loihi, SpiNNaker, memristive crossbars
6. **Applications** — event-based vision, robotics, edge inference
7. **Challenges & Future Directions**
8. **Conclusion**

## 🗂️ Repository Structure

```
snn-survey/
├── main.tex            # Main LaTeX document
├── references.bib      # Bibliography (BibTeX)
├── sections/           # One .tex file per section
│   ├── 00_abstract.tex
│   ├── 01_introduction.tex
│   └── ...
├── figures/            # Figures and diagrams
└── README.md
```

## 🛠️ Building the PDF

Requires a LaTeX distribution (e.g., TeX Live or MiKTeX).

```bash
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

Or, with `latexmk`:

```bash
latexmk -pdf main.tex
```

## 🤝 Contributing

Contributions are welcome! Please add references to `references.bib` and expand
the relevant section under `sections/`. Open a pull request with a short
description of what you added.

## 📜 License

This work is released under the [MIT License](LICENSE).
