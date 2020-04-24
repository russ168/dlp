from dlp.analyzer_engine import AnalyzerEngine

analyzer = AnalyzerEngine(enable_trace_pii=True)

text_to_scan = "Here is a dummy number : 5160-750024596780"
results = analyzer.analyze(correlation_id=1,
                           text=text_to_scan,
                           entities=["CREDIT_CARD"],
                           language='en',
                           all_fields=False)


for item in results:
    print("Detected = {}, Start = {}, end = {}, entity = {}, confidence = {}".format(text_to_scan[item.start: item.end],
                                                                                     item.start,
                                                                                     item.end,
                                                                                     item.entity_type,
                                                                                     item.score))
