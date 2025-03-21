import time
import statistics
import tiktoken

def benchmark_encoding(text, encoding_name="cl100k_base", runs=5):
    """Run encoding benchmark multiple times and return statistics."""
    encoder = tiktoken.get_encoding(encoding_name)
    times = []
    
    for i in range(runs):
        start_time = time.time()
        tokens = encoder.encode(text)
        end_time = time.time()
        times.append(end_time - start_time)
        
    return {
        'token_count': len(tokens),
        'avg_time': sum(times) / len(times),
        'min_time': min(times),
        'max_time': max(times),
        'median_time': statistics.median(times),
        'times': times
    }

# Test cases
test_cases = [
    # Regular English text
    {
        'name': 'English Essay',
        'text': '''
        The quick brown fox jumps over the lazy dog. This sentence contains every letter of the English alphabet.
        Natural language processing has evolved significantly over the past decade. With the advent of transformer models,
        we've seen remarkable improvements in various NLP tasks such as translation, summarization, and question answering.
        These models leverage attention mechanisms to process text in parallel rather than sequentially, allowing for more
        efficient training and inference. While traditional recurrent neural networks (RNNs) and long short-term memory (LSTM)
        networks process text one token at a time, transformers can attend to all tokens simultaneously, capturing long-range
        dependencies more effectively. The development of pre-training techniques has also contributed to the success of
        modern NLP systems. By pre-training models on large corpora of text, researchers have been able to develop models
        that possess a form of general language understanding, which can then be fine-tuned for specific downstream tasks.
        This approach has led to the creation of models like BERT, GPT, and T5, each with their own unique architecture
        and capabilities. Despite these advances, challenges remain in the field of NLP. Issues such as bias in training
        data, the environmental impact of training large models, and the need for more efficient architectures continue
        to drive research in this area. As we move forward, it's likely that we'll see a continued focus on developing
        models that are not only more powerful but also more efficient and ethical.
        ''' * 100  # Repeat to make it longer
    },
    
    # Code
    {
        'name': 'Python Code',
        'text': '''
def quicksort(arr):
    """
    Implement quicksort algorithm to sort an array
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

def merge_sort(arr):
    """
    Implement merge sort algorithm
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)
    
def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
        ''' * 50  # Repeat to make it longer
    },
    
    # Mixed content with some repetition but not excessive
    {
        'name': 'Mixed Content',
        'text': '''
        <html>
        <head>
            <title>Sample Document</title>
        </head>
        <body>
            <h1>Welcome to the Sample Page</h1>
            <p>This is a paragraph with some text. It also contains some repeated content like:</p>
            <ul>
                <li>Item one</li>
                <li>Item two</li>
                <li>Item three</li>
            </ul>
            <p>And here is a table:</p>
            <table>
                <tr><td>Row 1, Col 1</td><td>Row 1, Col 2</td></tr>
                <tr><td>Row 2, Col 1</td><td>Row 2, Col 2</td></tr>
                <tr><td>Row 3, Col 1</td><td>Row 3, Col 2</td></tr>
            </table>
            <div class="repeated">
                This div has some moderately repeated content.
                This div has some moderately repeated content.
                This div has some moderately repeated content.
            </div>
            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor 
                incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
                exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            </p>
        </body>
        </html>
        ''' * 30  # Repeat to make it longer
    },
    
    # Moderate repetition (but not pathological)
    {
        'name': 'Moderate Repetition',
        'text': 'The word "repeated" is repeated repeatedly in this repeated text with repeated repetition of the repeated word "repeated". ' * 100
    }
]

print("\nRunning benchmarks on various text types...\n")

for test in test_cases:
    print(f"Testing: {test['name']}")
    print(f"Text length: {len(test['text'])} characters")
    
    results = benchmark_encoding(test['text'])
    
    print(f"Token count: {results['token_count']}")
    print(f"Average time: {results['avg_time']:.4f} seconds")
    print(f"Min time: {results['min_time']:.4f} seconds")
    print(f"Max time: {results['max_time']:.4f} seconds")
    print(f"Median time: {results['median_time']:.4f} seconds")
    print(f"Tokens per second: {results['token_count'] / results['avg_time']:.2f}")
    print("\n" + "-"*80 + "\n")

print("Benchmarks completed!")
