#!/usr/bin/env python3
"""
CLI Browser for Wzorce from piszemywirale.pl

Interactive command-line tool to browse and search viral post patterns.
"""

import json
import sys
from typing import List, Dict

def load_data():
    """Load the wzorce data."""
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
    """List all wzorce with numbers."""
    print("\n📚 Wzorce z piszemywirale.pl:\n")
    for i, pt in enumerate(data['postTypes'], 1):
        print(f"{i:3d}. Wzorzec #{pt['number']}")
        # Show first 80 chars of type description
        type_preview = pt['type'][:80] + "..." if len(pt['type']) > 80 else pt['type']
        print(f"      {type_preview}")
        print()

def show_post_details(post: Dict):
    """Show detailed information about a wzorzec."""
    print_separator()
    print(f"📌 WZORZEC #{post['number']}")
    print_separator()
    print(f"\n🆔 ID: {post['id']}")
    print(f"\n📝 TYP POSTA:")
    print_separator('-')
    # Wrap text at reasonable length
    type_text = post['type']
    for i in range(0, len(type_text), 100):
        print(type_text[i:i+100])
    print_separator('-')
    
    print(f"\n🧠 DLACZEGO TO DZIAŁA (Psychologia i Algorytm):")
    print_separator('-')
    why_text = post['why']
    for i in range(0, len(why_text), 100):
        print(why_text[i:i+100])
    print_separator('-')

def search_posts(data: Dict, query: str) -> List[Dict]:
    """Search wzorce by content."""
    query = query.lower()
    results = []
    
    for pt in data['postTypes']:
        # Search in type and why descriptions
        if (query in pt['type'].lower() or 
            query in pt['why'].lower() or
            query in pt['id'].lower()):
            results.append(pt)
    
    return results

def show_stats(data: Dict):
    """Show statistics about the library."""
    print("\n📊 Statystyki Biblioteki:\n")
    print(f"  Wzorców: {data['metadata']['totalTypes']}")
    print(f"  Źródło: {data['metadata']['source']}")
    print(f"  Język: {data['metadata']['language']}")
    print(f"  Ostatnia aktualizacja: {data['metadata']['lastUpdated']}")
    print(f"  Wersja: {data['metadata']['version']}")

def interactive_mode(data: Dict):
    """Run interactive CLI browser."""
    while True:
        print("\n" + "=" * 70)
        print("🚀 WIRALOWNIA - Browser Wzorców z piszemywirale.pl")
        print("=" * 70)
        print("\nOpcje:")
        print("  1. Lista wszystkich wzorców")
        print("  2. Pokaż szczegóły wzorca (po numerze)")
        print("  3. Szukaj wzorców")
        print("  4. Statystyki")
        print("  0. Wyjście")
        print()
        
        choice = input("Wybierz opcję [0-4]: ").strip()
        
        if choice == '0':
            print("\n👋 Do zobaczenia!\n")
            break
        
        elif choice == '1':
            list_all_types(data)
            input("\nNaciśnij Enter aby kontynuować...")
        
        elif choice == '2':
            try:
                num = int(input(f"\nPodaj numer wzorca (1-{len(data['postTypes'])}): ").strip())
                if 1 <= num <= len(data['postTypes']):
                    show_post_details(data['postTypes'][num - 1])
                    input("\nNaciśnij Enter aby kontynuować...")
                else:
                    print(f"❌ Numer musi być między 1 a {len(data['postTypes'])}")
            except ValueError:
                print("❌ Podaj prawidłowy numer")
        
        elif choice == '3':
            query = input("\nSzukaj (słowo kluczowe): ").strip()
            results = search_posts(data, query)
            if results:
                print(f"\n✅ Znaleziono {len(results)} wzorców:\n")
                for i, pt in enumerate(results, 1):
                    type_preview = pt['type'][:60] + "..." if len(pt['type']) > 60 else pt['type']
                    print(f"{i}. Wzorzec #{pt['number']}: {type_preview}")
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
            show_stats(data)
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
                    type_preview = pt['type'][:80] + "..." if len(pt['type']) > 80 else pt['type']
                    print(f"Wzorzec #{pt['number']} ({pt['id']}): {type_preview}")
            else:
                print(f"No results for: {query}")
        
        elif command == 'show' and len(sys.argv) > 2:
            try:
                # Try by number first
                num = int(sys.argv[2])
                if 1 <= num <= len(data['postTypes']):
                    show_post_details(data['postTypes'][num - 1])
                else:
                    print(f"Wzorzec number must be between 1 and {len(data['postTypes'])}")
            except ValueError:
                # Try by ID
                wzorzec_id = sys.argv[2]
                for pt in data['postTypes']:
                    if pt['id'] == wzorzec_id:
                        show_post_details(pt)
                        break
                else:
                    print(f"Wzorzec not found: {wzorzec_id}")
        
        elif command == 'stats':
            show_stats(data)
        
        else:
            print("Usage:")
            print("  Interactive mode:  python browser.py")
            print("  List all:          python browser.py list")
            print("  Search:            python browser.py search <query>")
            print("  Show details:      python browser.py show <number|id>")
            print("  Show stats:        python browser.py stats")
    
    else:
        # Interactive mode
        interactive_mode(data)

if __name__ == '__main__':
    main()
