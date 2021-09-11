from .graph import Undirected_Graph

def page_rank_algorithm(graph, damping_factor = 0.85, num_iter = 1000):
    """Implement the classic Page Rank algorithm of Google"""
    # The list of web pages to be ranked
    webpages = graph.get_vertices()

    # The probability of landing in a particular web page
    # All initialized to 1 / number of web pages
    probs = {}
    for webpage in webpages:
        probs[webpage] = 1 / len(webpages)

    for iter in range(num_iter):
        # The starting probabilities for next iteration
        next_probs = {}
        for webpage in probs:
            next_probs[webpage] = 0

        # Initially there is a probability of prob to land in cur_webpage
        for (cur_webpage, prob) in probs.items():
            neighbours = graph.get_neighbours(cur_webpage)

            # Normal Case: The user has a probability of damping_factor to move to a linked webpage
            # In which case the probability of moving to neighbour is given by edge weight
            # There is also a probability of 1-damping_factor to not click any links in cur_webpage
            # In which case the user will switch to a random webpage at equal probability
            if (neighbours != []):
                for (neighbour, weight) in neighbours:
                    next_probs[neighbour] += prob * damping_factor * weight
                for webpage in next_probs:
                    next_probs[webpage] += prob * (1 - damping_factor) * (1 / len(webpages))
            
            # Special Case: The current webpage might have no links,
            # In which case the user will switch to a random webpage at equal probability
            else:
                for webpage in next_probs:
                    next_probs[webpage] += prob * (1 / len(webpages))

        probs = next_probs

    # Sort the webpages by decreasing order of probability
    ranked_webpages = list(sorted(probs.items(), key = lambda kvp: kvp[1], reverse = True))

    return ranked_webpages
