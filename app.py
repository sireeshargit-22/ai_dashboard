from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.h2("AI Analysis Dashboard using python shiny"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select(
                "model_choice",
                "Select AI Model:",
                choices=["GPT", "BERT", "Transformer", "LSTM"]
            ),
            ui.input_slider("data_size", "Dataset Size (MB):", 10, 1000, 100),
            ui.input_action_button("analyze", "Run Analysis")
        ),
        ui.panel_main(
            ui.output_text("summary"),
            ui.output_plot("performance_plot")
        )
    )
)

def server(input, output, session):
    @output
    @render.text
    def summary():
        return f"Model: {input.model_choice()}, Dataset Size: {input.data_size()} MB"

    @output
    @render.plot
    def performance_plot():
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.arange(1, 6)
        y = np.random.rand(5) * input.data_size() / 100
        plt.bar(x, y, color="skyblue")
        plt.title(f"{input.model_choice()} Performance Metrics")
        plt.xlabel("Metric Index")
        plt.ylabel("Score")
        return plt.gcf()

app = App(app_ui, server)
