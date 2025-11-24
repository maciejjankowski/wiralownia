#!/usr/bin/env python3
"""
Example usage of wzorce from piszemywirale.pl

This script demonstrates how to programmatically access and use
the viral post patterns library.
"""

import json
from typing import List, Dict

def load_wzorce(filename: str = 'post-types.json') -> Dict:
    """Load wzorce from JSON file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_wzorzec_by_number(data: Dict, number: int) -> Dict:
    """Get a specific wzorzec by number."""
    for wzorzec in data['postTypes']:
        if wzorzec['number'] == number:
            return wzorzec
    return None

def get_wzorzec_by_id(data: Dict, wzorzec_id: str) -> Dict:
    """Get a specific wzorzec by ID."""
    for wzorzec in data['postTypes']:
        if wzorzec['id'] == wzorzec_id:
            return wzorzec
    return None

def search_wzorce(data: Dict, keyword: str) -> List[Dict]:
    """Search wzorce by keyword in type or why descriptions."""
    keyword = keyword.lower()
    return [
        w for w in data['postTypes']
        if keyword in w['type'].lower() or keyword in w['why'].lower()
    ]

def main():
    # Load data
    data = load_wzorce()
    
    print(f"📚 Loaded {len(data['postTypes'])} wzorce from {data['metadata']['source']}\n")
    
    # Example 1: Get a specific wzorzec by number
    print("=" * 70)
    print("Example 1: Get wzorzec #1")
    print("=" * 70)
    wzorzec1 = get_wzorzec_by_number(data, 1)
    if wzorzec1:
        print(f"ID: {wzorzec1['id']}")
        print(f"Type (first 100 chars): {wzorzec1['type'][:100]}...")
        print(f"Why (first 100 chars): {wzorzec1['why'][:100]}...")
        print()
    
    # Example 2: Search for wzorce about vulnerability
    print("=" * 70)
    print("Example 2: Search for wzorce about 'vulnerability'")
    print("=" * 70)
    vulnerability_posts = search_wzorce(data, 'vulnerability')
    print(f"Found {len(vulnerability_posts)} wzorce mentioning vulnerability:\n")
    for w in vulnerability_posts[:3]:  # Show first 3
        print(f"Wzorzec #{w['number']}: {w['type'][:80]}...")
    print()
    
    # Example 3: Search for wzorce about humor
    print("=" * 70)
    print("Example 3: Search for wzorce about 'humor'")
    print("=" * 70)
    humor_posts = search_wzorce(data, 'humor')
    print(f"Found {len(humor_posts)} wzorce mentioning humor:\n")
    for w in humor_posts[:3]:  # Show first 3
        print(f"Wzorzec #{w['number']}: {w['type'][:80]}...")
    print()
    
    # Example 4: Get wzorce about LinkedIn algorithm
    print("=" * 70)
    print("Example 4: Search for wzorce about 'algorytm'")
    print("=" * 70)
    algorithm_posts = search_wzorce(data, 'algorytm')
    print(f"Found {len(algorithm_posts)} wzorce mentioning algorithm")
    print()
    
    # Example 5: Statistics
    print("=" * 70)
    print("Example 5: Library Statistics")
    print("=" * 70)
    print(f"Total wzorce: {data['metadata']['totalTypes']}")
    print(f"Source: {data['metadata']['source']}")
    print(f"Language: {data['metadata']['language']}")
    print(f"Last updated: {data['metadata']['lastUpdated']}")
    print(f"Version: {data['metadata']['version']}")
    print()
    
    # Example 6: Show all wzorce numbers
    print("=" * 70)
    print("Example 6: First 10 wzorce")
    print("=" * 70)
    for w in data['postTypes'][:10]:
        print(f"{w['number']:3d}. {w['type'][:70]}...")
    print()

if __name__ == '__main__':
    main()
