import seaborn as sns
import matplotlib.pyplot as plt


def plot_line_graph(df, x, y, x_label, y_label, title):
    plt.figure(figsize=(10, 6))
    sns.set_theme()
    sns.lineplot(data=df, x=x, y=y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def plot_pie_chart(df, labels, title):
    plt.figure(figsize=(8, 8))
    plt.pie(
        df,
        labels=labels,
        autopct="%1.1f%%",
        startangle=140,
        colors=sns.color_palette("viridis", len(labels)),
    )
    plt.title(title)


def plot_bar_chart(df, x, y, x_label, y_label, title):
    plt.figure(figsize=(10, 6))
    sns.set_theme()
    sns.barplot(x=x, y=y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
