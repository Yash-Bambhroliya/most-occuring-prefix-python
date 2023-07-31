def add_prefixes_to_dict(word, prefixes_dict):
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            prefix = word[i:j]
            if len(prefix) == len(word):  # Exclude the word itself
                break
            elif len(prefix) > 1:  # Exclude single characters
                prefixes_dict[prefix] = prefixes_dict.get(prefix, 0) + 1

def top_three_most_occurring_prefixes(prefixes_dict):
    return dict(sorted(prefixes_dict.items(), key=lambda x: -x[1])[:3]) # Sort the dictionary by count (descending) and return the top 3

def count_word_prefixes(paragraph):
    words = paragraph.split()
    prefixes_dict = {}

    for word in words:
        word = ''.join(char for char in word if char not in '!@#$%^&*()_+=[]{}\|;:\'"<>?,./') # Remove punctuations
        add_prefixes_to_dict(word, prefixes_dict)

    # Sort the dictionary by length of keys (descending) and count (descending)
    sorted_prefixes = sorted(prefixes_dict.items(), key=lambda x: (-len(x[0]), -x[1])) # Sort the dictionary by length of keys (descending) and count (descending)

    # Create a new dictionary to store the three longest prefixes with the highest occurrence
    top_three_prefixes = {}
    for prefix, count in sorted_prefixes:
        if len(top_three_prefixes) == 3:
            break
        top_three_prefixes[prefix] = count

    # print(prefixes_dict)

    # Top 3 most occurring prefixes by count regardless of length
    print("Top 3 most occurring prefixes: ", top_three_most_occurring_prefixes(prefixes_dict))

    return top_three_prefixes

if __name__ == "__main__":
    # paragraph = input("Enter the paragraph: ")
    paragraph = """Once upon a time, in a mystical forest, there lived a curious young fox named Finn. He loved exploring new places and making friends with all creatures. One day, he stumbled upon a hidden cave guarded by an ancient owl. The owl revealed a magical map leading to a lost treasure. Excited, Finn embarked on a thrilling adventure, facing challenges and discovering the true meaning of bravery and friendship. Along the journey, he met Ruby, a wise tortoise, and Milo, a mischievous raccoon. Together, they solved riddles, crossed dangerous rivers, and battled a cunning wolf. In the end, they found the treasure - not gold, but the knowledge that true treasure lies in the hearts of friends. They returned home as heroes, cherishing their incredible journey forever. The forest echoed with laughter and tales of their legendary adventure. In a small coastal town, lived a young girl named Lily, who was fascinated by the ocean. One night, a mysterious seashell washed ashore, whispering secrets of an enchanted underwater kingdom. The shell led her to a hidden cave where a mermaid named Marina awaited. Marina told Lily about a rare moonstone that held immense power to heal the ocean. The evil sea witch, Morgana, had stolen it, causing the sea's decline. Lily, determined to help, embarked on a perilous quest with Marina and her loyal seahorse, Splash. They faced treacherous sea creatures and solved puzzles in ancient ruins. With courage and kindness, they confronted Morgana. In an epic battle, Lily used the moonstone's magic to restore the ocean's health, driving out Morgana's darkness. As gratitude, the underwater creatures bestowed upon Lily the gift of understanding sea whispers. Lily returned home, forever changed by her magical journey, vowing to protect the ocean and its wonders. From that day on, whenever she strolled along the shore, the waves seemed to dance and sing just for her. In the heart of a vast jungle, lived a young elephant named Kavi. He dreamt of soaring high like the birds he saw above the treetops. One day, an ancient parrot gave him magical feathers, unlocking the power of flight. Kavi's soaring adventures took him to breathtaking heights, witnessing the beauty of the world. Yet, he realized his true happiness was with his herd. Kavi returned, cherishing both his soaring dreams and the love of his family, forever. In a whimsical kingdom, twins Luna and Leo possessed extraordinary powers - night and day. One day, a sinister sorceress stole their abilities, casting darkness over the land. To reclaim their gifts, they embarked on a courageous journey, learning to embrace each other's strengths. Their unity defeated the sorceress, restoring balance, and teaching the kingdom the power of harmony. In a quaint village, there lived an imaginative girl named Ava. She found a magic book that transported her to enchanted realms. From enchanted forests to floating islands, Ava's adventures were boundless. As she uncovered secrets, she realized the book was her portal to self-discovery. Each chapter taught her valuable lessons, empowering her to create her own magical story. And so, Ava became the author of her fantastical destiny."""
    top_three_prefixes = count_word_prefixes(paragraph)

    # Print the result
    print("Top 3 longest prefixes with highest occurrence: ")
    for prefix, count in top_three_prefixes.items():
        print(f'"{prefix}": {count}')
