class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_emoji = False
        self.emoji = None

class EmojiTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, keyword, emoji):
        node = self.root
        for char in keyword:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_emoji = True
        node.emoji = emoji

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_emojis(node)

    def _find_emojis(self, node):
        emojis = []
        if node.is_end_of_emoji:
            emojis.append(node.emoji)
        for child in node.children.values():
            emojis.extend(self._find_emojis(child))
        return emojis


emoji_trie = EmojiTrie()

emoji_data = {
    "smile": "😃",
    "sad": "😢",
    "heart": "❤️",
    "shock": "😳",
    "time": "🕖",
    "thumbs up": "👍",
    "fire": "🔥",
    "star": "⭐",
    "sun": "☀️",
    "moon": "🌙",
    "ok": "✔️",
    "wrong": "❌",
    "clap": "👏",
    "wave": "👋",
    "laugh": "😂",
    "cry": "😭",
    "angry": "😡",
    "kiss": "😘",
    "thinking": "🤔",
    "party": "🎉",
    "gift": "🎁",
    "music": "🎵",
    "cat": "🐱",
    "dog": "🐶",
    "rose": "🌹",
    "tree": "🌳",
    "earth": "🌍",
    "rocket": "🚀",
    "car": "🚗",
    "computer": "💻",
    "phone": "📱",
    "book": "📚",
    "coffee": "☕",
    "pizza": "🍕",
    "ice cream": "🍦",
    "cake": "🍰",
    "beer": "🍺",
    "wine": "🍷",
    "flag": "🏳️",
    "soccer": "⚽",
    "basketball": "🏀",
    "guitar": "🎸",
    "piano": "🎹",
    "drum": "🥁",
}

for keyword, emoji in emoji_data.items():
    emoji_trie.insert(keyword, emoji)

def main():
    print("Welcome to the Emoji Autocomplete System!")
    print("Type a keyword to get emoji suggestions or 'exit' to quit.")
    
    recent_emojis = []  # List to maintain order of recent emojis
    max_recent = 10  # Maximum number of recent emojis to display

    while True:
        user_input = input("Enter keyword: ").strip().lower()
        
        # Error handling for empty input
        if not user_input:
            print("Input cannot be empty. Please enter a keyword.")
            continue
        
        # Error handling for non-alphabetic characters
        if not user_input.replace(" ", "").isalpha():
            print("Please enter a valid keyword containing only alphabetic characters.")
            continue
        
        if user_input == 'exit':
            print("Exiting the Emoji Autocomplete System. Goodbye!")
            break
        
        suggestions = emoji_trie.autocomplete(user_input)
        
        if suggestions:
            print("Suggestions:")
            for index, suggestion in enumerate(suggestions):
                print(f"{index + 1}: {suggestion}")
            
            # Allow user to select a suggestion
            while True:
                try:
                    choice = int(input("Select an emoji by number (or 0 to cancel): "))
                    if choice == 0:
                        print("Selection canceled.")
                        break
                    if 1 <= choice <= len(suggestions):
                        selected_emoji = suggestions[choice - 1]
                        
                        # Update recent emojis list
                        if selected_emoji in recent_emojis:
                            recent_emojis.remove(selected_emoji)  # Remove if already exists
                        recent_emojis.insert(0, selected_emoji)  # Add to the start
                        if len(recent_emojis) > max_recent:
                            recent_emojis.pop()  # Maintain maximum recent limit
                        
                        print(f"You selected: {selected_emoji}")
                        print(f"Recent emojis: {', '.join(recent_emojis)}")
                        break
                    else:
                        print("Invalid choice. Please select a valid number.")
                except ValueError:
                    print("Please enter a number.")
        else:
            print("No suggestions found. Please try refining your keyword.")

if __name__ == "__main__":
    main()
