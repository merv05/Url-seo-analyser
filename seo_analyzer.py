import seo_utils
import seo_visualizer

def analyze_webpage(url):
    content = seo_utils.fetch_webpage(url)
    if not content:
        return None

    soup = seo_utils.parse_html(content)
    text = soup.get_text()

    word_count, word_freq = seo_utils.get_word_count(text)
    title, description = seo_utils.get_meta_tags(soup)
    headers = seo_utils.analyze_headers(soup)
    total_images, images_with_alt = seo_utils.analyze_images(soup)
    internal_links, external_links = seo_utils.analyze_links(soup, url)
    keyword_density = seo_utils.calculate_keyword_density(word_freq, word_count)

    seo_score = calculate_seo_score(title, description, word_count, headers, images_with_alt, total_images)

    return {
        "url": url,
        "title": title,
        "description": description,
        "word_count": word_count,
        "keyword_density": keyword_density,
        "headers": headers,
        "images": (total_images, images_with_alt),
        "links": (internal_links, external_links),
        "seo_score": seo_score
    }

def calculate_seo_score(title, description, word_count, headers, images_with_alt, total_images):
    score = 0
    if len(title) > 10 and len(title) < 60:
        score += 10
    if len(description) > 50 and len(description) < 160:
        score += 10
    if word_count > 300:
        score += 10
    if headers['h1'] == 1:
        score += 10
    if sum(headers.values()) > 3:
        score += 10
    if images_with_alt == total_images and total_images > 0:
        score += 10
    return score

if __name__ == "__main__":
    url = input("Enter a URL to analyze: ")
    results = analyze_webpage(url)
    if results:
        seo_visualizer.visualize_results(results)
