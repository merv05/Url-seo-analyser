import matplotlib.pyplot as plt
import numpy as np

def visualize_results(results):
    plt.figure(figsize=(15, 10))
    plt.suptitle(f"SEO Analysis for {results['url']}", fontsize=16)

    # Keyword Density
    plt.subplot(2, 2, 1)
    words, frequencies, _ = zip(*results['keyword_density'])
    plt.bar(words, frequencies)
    plt.title('Top 10 Keywords')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Frequency')

    # Header Distribution
    plt.subplot(2, 2, 2)
    headers = results['headers']
    plt.bar(headers.keys(), headers.values())
    plt.title('Header Tag Distribution')
    plt.ylabel('Count')

    # Links and Images
    plt.subplot(2, 2, 3)
    internal_links, external_links = results['links']
    total_images, images_with_alt = results['images']
    categories = ['Internal Links', 'External Links', 'Images with Alt', 'Images without Alt']
    values = [internal_links, external_links, images_with_alt, total_images - images_with_alt]
    plt.bar(categories, values)
    plt.title('Links and Images')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Count')

    # SEO Score
    plt.subplot(2, 2, 4)
    seo_score = results['seo_score']
    plt.pie([seo_score, 100-seo_score], labels=['Score', 'Remaining'], autopct='%1.1f%%', startangle=90)
    plt.title(f'SEO Score: {seo_score}/100')

    # Text information
    plt.figtext(0.5, 0.02, f"Title: {results['title']}\nDescription: {results['description']}\nWord Count: {results['word_count']}", 
                ha="center", fontsize=10, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})

    plt.tight_layout()
    plt.show()
