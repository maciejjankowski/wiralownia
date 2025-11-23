#!/usr/bin/env python3
"""
Example usage of post-types.json data

This script demonstrates how to programmatically access and use
the viral post types library.
"""

import json
from typing import List, Dict

def load_post_types(filename: str = 'post-types.json') -> Dict:
    """Load post types from JSON file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_post_type_by_id(data: Dict, post_id: str) -> Dict:
    """Get a specific post type by ID."""
    for post_type in data['postTypes']:
        if post_type['id'] == post_id:
            return post_type
    return None

def get_post_types_by_category(data: Dict, category: str) -> List[Dict]:
    """Get all post types in a specific category."""
    return [pt for pt in data['postTypes'] if pt['category'] == category]

def get_post_types_by_platform(data: Dict, platform: str) -> List[Dict]:
    """Get post types recommended for a specific platform."""
    return [pt for pt in data['postTypes'] if platform in pt['bestFor']]

def generate_prompt(post_type: Dict, variables: Dict[str, str]) -> str:
    """
    Generate a customized prompt by replacing variables.
    
    Args:
        post_type: The post type dictionary
        variables: Dict of variable replacements, e.g., {'TEMAT': 'Marketing AI'}
    
    Returns:
        Customized prompt with variables replaced
    """
    prompt = post_type['prompt']
    for key, value in variables.items():
        prompt = prompt.replace(f'[{key}]', value)
    return prompt

def main():
    # Load data
    data = load_post_types()
    
    print(f"📚 Loaded {len(data['postTypes'])} post types\n")
    
    # Example 1: Get a specific post type
    print("=" * 60)
    print("Example 1: Get 'Tutorial' post type")
    print("=" * 60)
    tutorial = get_post_type_by_id(data, 'tutorial')
    if tutorial:
        print(f"Name: {tutorial['name']}")
        print(f"Category: {tutorial['category']}")
        print(f"Best platforms: {', '.join(tutorial['bestFor'])}")
        print()
    
    # Example 2: Get all educational posts
    print("=" * 60)
    print("Example 2: Educational post types")
    print("=" * 60)
    educational = get_post_types_by_category(data, 'educational')
    for post in educational:
        print(f"- {post['name']} ({post['id']})")
    print()
    
    # Example 3: Get posts suitable for LinkedIn
    print("=" * 60)
    print("Example 3: Posts recommended for LinkedIn")
    print("=" * 60)
    linkedin_posts = get_post_types_by_platform(data, 'LinkedIn')
    for post in linkedin_posts:
        print(f"- {post['name']}")
    print()
    
    # Example 4: Generate customized prompt
    print("=" * 60)
    print("Example 4: Generate customized tutorial prompt")
    print("=" * 60)
    custom_prompt = generate_prompt(tutorial, {
        'TEMAT': 'zwiększanie zaangażowania na Instagramie',
        'LICZBA': '5',
        'POZIOM': 'POCZĄTKUJĄCY',
        'FORMAT': 'GRAFIKA'
    })
    print(custom_prompt[:300] + "...")
    print()
    
    # Example 5: List all categories
    print("=" * 60)
    print("Example 5: Available categories")
    print("=" * 60)
    categories = data['metadata']['categories']
    for i, category in enumerate(categories, 1):
        count = len(get_post_types_by_category(data, category))
        print(f"{i}. {category} ({count} post types)")
    print()
    
    # Example 6: Statistics
    print("=" * 60)
    print("Example 6: Library Statistics")
    print("=" * 60)
    print(f"Total post types: {data['metadata']['totalTypes']}")
    print(f"Categories: {len(data['metadata']['categories'])}")
    print(f"Platforms covered: {len(data['metadata']['platforms'])}")
    print(f"Language: {data['metadata']['language']}")
    print(f"Last updated: {data['metadata']['lastUpdated']}")
    print()

if __name__ == '__main__':
    main()
