#!/usr/bin/env python3
"""
CLI Browser for Viral Post Types

Interactive command-line tool to browse, search, and get prompts
from the viral post types library.
"""

import json
import sys
from typing import List, Dict

def load_data():
    """Load the post types data."""
    try:
        with open('post-types.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: post-types.json not found!")
        sys.exit(1)

def print_separator(char='=', length=70):
    """Print a separator line."""
    print(char * length)

def list_all_types(data: Dict):
    """List all post types with numbers."""
    print("\n📚 Available Post Types:\n")
    for i, pt in enumerate(data['postTypes'], 1):
        category_emoji = {
            'storytelling': '📖',
            'educational': '🎓',
            'interactive': '🎮',
            'entertainment': '😂',
            'social-proof': '💼',
            'visual-educational': '🎨',
            'engagement': '💬',
            'inspirational': '⭐',
            'authentic': '🎬',
            'resources': '📚',
            'data-driven': '📊',
            'thought-leadership': '🔮'
        }
        emoji = category_emoji.get(pt['category'], '📝')
        print(f"{i:2d}. {emoji} {pt['name']}")
        print(f"    ID: {pt['id']} | Kategoria: {pt['category']}")
        print(f"    Platformy: {', '.join(pt['bestFor'][:3])}")
        print()

def show_post_details(post: Dict):
    """Show detailed information about a post type."""
    print_separator()
    print(f"📌 {post['name'].upper()}")
    print_separator()
    print(f"\n🆔 ID: {post['id']}")
    print(f"📂 Kategoria: {post['category']}")
    print(f"\n📝 Opis:")
    print(f"   {post['description']}")
    
    print(f"\n🏗️  Struktura:")
    for i, step in enumerate(post['structure'], 1):
        print(f"   {i}. {step}")
    
    print(f"\n💡 Przykłady:")
    for example in post['examples']:
        print(f"   • {example}")
    
    print(f"\n📱 Najlepsze platformy:")
    for platform in post['bestFor']:
        print(f"   ✓ {platform}")
    
    print(f"\n🚀 Czynniki wiralności:")
    for factor in post['viralityFactors']:
        print(f"   ⭐ {factor}")
    
    print(f"\n📋 PROMPT:")
    print_separator('-')
    print(post['prompt'])
    print_separator('-')

def search_posts(data: Dict, query: str) -> List[Dict]:
    """Search posts by name, category, or platform."""
    query = query.lower()
    results = []
    
    for pt in data['postTypes']:
        # Search in name, description, category
        if (query in pt['name'].lower() or 
            query in pt['description'].lower() or
            query in pt['category'].lower() or
            query in pt['id'].lower()):
            results.append(pt)
            continue
        
        # Search in platforms
        for platform in pt['bestFor']:
            if query in platform.lower():
                results.append(pt)
                break
    
    return results

def show_categories(data: Dict):
    """Show all categories with post counts."""
    print("\n📂 Kategorie:\n")
    categories = {}
    for pt in data['postTypes']:
        cat = pt['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(pt)
    
    for i, (cat, posts) in enumerate(sorted(categories.items()), 1):
        print(f"{i:2d}. {cat} ({len(posts)} wzorców)")
        for pt in posts:
            print(f"     • {pt['name']}")
        print()

def show_platforms(data: Dict):
    """Show all platforms with recommended post types."""
    print("\n📱 Platformy:\n")
    platforms = {}
    for pt in data['postTypes']:
        for platform in pt['bestFor']:
            if platform not in platforms:
                platforms[platform] = []
            platforms[platform].append(pt['name'])
    
    for i, (platform, posts) in enumerate(sorted(platforms.items()), 1):
        print(f"{i}. {platform} ({len(posts)} wzorców)")
        for post_name in posts[:5]:  # Show first 5
            print(f"   • {post_name}")
        if len(posts) > 5:
            print(f"   ... i {len(posts) - 5} więcej")
        print()

def interactive_mode(data: Dict):
    """Run interactive CLI browser."""
    while True:
        print("\n" + "=" * 70)
        print("🚀 WIRALOWNIA - Browser Wzorców Postów")
        print("=" * 70)
        print("\nOpcje:")
        print("  1. Lista wszystkich wzorców")
        print("  2. Pokaż szczegóły wzorca (po numerze)")
        print("  3. Szukaj wzorców")
        print("  4. Pokaż kategorie")
        print("  5. Pokaż platformy")
        print("  6. Statystyki")
        print("  0. Wyjście")
        print()
        
        choice = input("Wybierz opcję [0-6]: ").strip()
        
        if choice == '0':
            print("\n👋 Do zobaczenia!\n")
            break
        
        elif choice == '1':
            list_all_types(data)
            input("\nNaciśnij Enter aby kontynuować...")
        
        elif choice == '2':
            try:
                num = int(input("\nPodaj numer wzorca (1-20): ").strip())
                if 1 <= num <= len(data['postTypes']):
                    show_post_details(data['postTypes'][num - 1])
                    input("\nNaciśnij Enter aby kontynuować...")
                else:
                    print(f"❌ Numer musi być między 1 a {len(data['postTypes'])}")
            except ValueError:
                print("❌ Podaj prawidłowy numer")
        
        elif choice == '3':
            query = input("\nSzukaj (nazwa, kategoria, platforma): ").strip()
            results = search_posts(data, query)
            if results:
                print(f"\n✅ Znaleziono {len(results)} wzorców:\n")
                for i, pt in enumerate(results, 1):
                    print(f"{i}. {pt['name']} ({pt['category']})")
                print()
                try:
                    detail = input("Pokaż szczegóły? (podaj numer lub Enter): ").strip()
                    if detail:
                        idx = int(detail) - 1
                        if 0 <= idx < len(results):
                            show_post_details(results[idx])
                except:
                    pass
            else:
                print(f"\n❌ Nie znaleziono wzorców dla: '{query}'")
            input("\nNaciśnij Enter aby kontynuować...")
        
        elif choice == '4':
            show_categories(data)
            input("\nNaciśnij Enter aby kontynuować...")
        
        elif choice == '5':
            show_platforms(data)
            input("\nNaciśnij Enter aby kontynuować...")
        
        elif choice == '6':
            print("\n📊 Statystyki Biblioteki:\n")
            print(f"  Wzorców: {data['metadata']['totalTypes']}")
            print(f"  Kategorii: {len(data['metadata']['categories'])}")
            print(f"  Platform: {len(data['metadata']['platforms'])}")
            print(f"  Język: {data['metadata']['language']}")
            print(f"  Ostatnia aktualizacja: {data['metadata']['lastUpdated']}")
            print(f"  Wersja: {data['metadata']['version']}")
            input("\nNaciśnij Enter aby kontynuować...")
        
        else:
            print("\n❌ Nieprawidłowa opcja")

def main():
    """Main entry point."""
    data = load_data()
    
    if len(sys.argv) > 1:
        # CLI mode with arguments
        command = sys.argv[1]
        
        if command == 'list':
            list_all_types(data)
        
        elif command == 'search' and len(sys.argv) > 2:
            query = ' '.join(sys.argv[2:])
            results = search_posts(data, query)
            if results:
                for pt in results:
                    print(f"• {pt['name']} ({pt['id']})")
            else:
                print(f"No results for: {query}")
        
        elif command == 'show' and len(sys.argv) > 2:
            post_id = sys.argv[2]
            for pt in data['postTypes']:
                if pt['id'] == post_id:
                    show_post_details(pt)
                    break
            else:
                print(f"Post type not found: {post_id}")
        
        elif command == 'categories':
            show_categories(data)
        
        elif command == 'platforms':
            show_platforms(data)
        
        else:
            print("Usage:")
            print("  Interactive mode:  python browser.py")
            print("  List all:          python browser.py list")
            print("  Search:            python browser.py search <query>")
            print("  Show details:      python browser.py show <id>")
            print("  Show categories:   python browser.py categories")
            print("  Show platforms:    python browser.py platforms")
    
    else:
        # Interactive mode
        interactive_mode(data)

if __name__ == '__main__':
    main()
