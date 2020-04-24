=====
Usage
=====



.. code-block:: python
    :linenos:

    from dlp.analyzer_engine import AnalyzerEngine

    analyzer = AnalyzerEngine(enable_trace_pii=True)

    # Example 1
    text_to_scan = "Here is a fake dummy number : 5160-750024596781. Note that we will not get any results here."
    results = analyzer.analyze(correlation_id=1,
                            text=text_to_scan,
                            entities=["CREDIT_CARD"],
                            language='en',
                            all_fields=False)


    for item in results:
        print("Detected = {}, Start = {}, end = {}, entity = {}".format(text_to_scan[item.start: item.end],
                                                                                        item.start,
                                                                                        item.end,
                                                                                        item.entity_type))

    # Example 2
    text_to_scan = "Check this now : 5160750024596780 or this 5160-750024596780 or maybe this 5160-75002459-6780"
    results = analyzer.analyze(correlation_id=1,
                            text=text_to_scan,
                            entities=["CREDIT_CARD"],
                            language='en',
                            all_fields=False)


    for item in results:
    print("Detected = {}, Start = {}, end = {}, entity = {}".format(text_to_scan[item.start: item.end],
                                                                                     item.start,
                                                                                     item.end,
                                                                                     item.entity_type))
