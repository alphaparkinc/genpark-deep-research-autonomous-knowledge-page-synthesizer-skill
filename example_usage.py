from client import DeepResearchAutonomousKnowledgePageSynthesizerClient

def main():
    client = DeepResearchAutonomousKnowledgePageSynthesizerClient()
    res = client.synthesize_multidimensional_sparkpage('Frontier Reasoning LLM Scaling Laws and Post-Training')
    print('Sparkpage: ' + res['sparkpage_id'] + ' | ' + res['research_topic'])
    print('Sources Analyzed: ' + str(res['analyzed_primary_sources_count']) + ' | Consensus: ' + str(res['multi_agent_consensus_score_pct']) + '%')
    print('Sections: ' + ', '.join(res['synthesized_sections'][:3]) + '...')
    print('Page URL: ' + res['interactive_sparkpage_url'])

if __name__ == '__main__':
    main()
