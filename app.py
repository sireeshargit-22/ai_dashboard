from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.h2("AI Analysis Dashboard using Python Shiny"),
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
            ui.output_table("performance_table")
        )
    )
)

def server(input, output, session):
    @output
    @render.text
    def summary():
        return f"Model: {input.model_choice()}, Dataset Size: {input.data_size()} MB"

    @output
    @render.table
    def performance_table():
        # Just a simple static table — no pandas/numpy
        return [
            ["Metric", "Score"],
            ["Accuracy", "0.85"],
            ["Precision", "0.80"],
            ["Recall", "0.78"],
            ["F1‑Score", "0.79"],
            ["Latency", "120ms"]
        ]

app = App(app_ui, server)
