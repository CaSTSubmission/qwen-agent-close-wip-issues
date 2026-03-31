#!/usr/bin/env python3
"""
Visualization script for Qwen-Agent Closed WIP Issues Analysis
"""

import json
import matplotlib.pyplot as plt

def load_data():
    """Load the JSON analysis data"""
    with open('qwen-agent-close-wip-report.json', 'r') as f:
        return json.load(f)

def create_repository_chart(data):
    """Create a bar chart of repositories with WIP issues"""
    repo_stats = data['repository_stats']
    
    # Filter repositories with non-zero counts for better visualization
    repos_with_issues = {k: v for k, v in repo_stats.items() if v > 0}
    
    if not repos_with_issues:
        print("No repositories with closed WIP issues found.")
        return
    
    # Shorten repository names for display
    short_names = [repo.split('/')[-1] for repo in repos_with_issues.keys()]
    counts = list(repos_with_issues.values())
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(short_names, counts, color='skyblue')
    
    # Add count labels on top of bars
    for bar, count in zip(bars, counts):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                str(count), ha='center', va='bottom')
    
    plt.title('Closed "Work in Progress" Issues by Repository', fontsize=14, fontweight='bold')
    plt.xlabel('Repository', fontsize=12)
    plt.ylabel('Number of Closed WIP Issues', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('repository_wip_issues.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"Chart saved as 'repository_wip_issues.png'")

def create_summary_statistics(data):
    """Print summary statistics"""
    print("\n" + "="*60)
    print("Qwen-Agent Closed WIP Issues Analysis - Summary")
    print("="*60)
    print(f"Analysis Date: {data['analysis_date']}")
    print(f"Total Repositories Analyzed: {data['total_repositories_analyzed']}")
    print(f"Total Closed WIP Issues: {data['total_closed_wip_issues']}")
    
    # Calculate percentage of repositories with WIP issues
    repo_stats = data['repository_stats']
    repos_with_issues = sum(1 for v in repo_stats.values() if v > 0)
    percentage = (repos_with_issues / len(repo_stats)) * 100
    
    print(f"Repositories with WIP Issues: {repos_with_issues} ({percentage:.1f}%)")
    print("\n" + "-"*60)
    print("Repositories with Closed WIP Issues:")
    print("-"*60)
    
    for repo, count in repo_stats.items():
        if count > 0:
            print(f"  • {repo}: {count} issue{'s' if count != 1 else ''}")
    
    print("\n" + "-"*60)
    print("Sample Issue Analysis:")
    print("-"*60)
    
    for issue in data['sample_wip_issues']:
        print(f"\nIssue #{issue['issue_number']}: {issue['title']}")
        print(f"  Created: {issue['created'][:10]}")
        print(f"  Closed: {issue['closed'][:10]}")
        print(f"  Duration: {issue['duration_days']} days")

def main():
    """Main function to run visualization"""
    print("Loading analysis data...")
    data = load_data()
    
    print("\nGenerating visualizations...")
    create_summary_statistics(data)
    create_repository_chart(data)
    
    print("\n" + "="*60)
    print("Analysis complete!")
    print("="*60)

if __name__ == "__main__":
    main()