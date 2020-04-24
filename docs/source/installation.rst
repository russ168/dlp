============
Installation
============


Clone the github repository:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    git clone https://github.com/ditordccaa/dlp.git


Creating the wheel file:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cd into the cloned folder and run:

::

    python setup.py bdist_wheel


Installing the wheel file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create an environment variable `WHEEL_FILE` the created wheel file (from the `dist` folder) into a clean virtual environment

::

    export WHEEL_FILE=path to the .whl file inside the dist folder


2. install `wheel` package

::

    pip install wheel


3. Install the wheel file

::

    pip install $WHEEL_FILE

Where `WHEEL_FILE` is the path to the created wheel file


4. Install the Spacy model (this is not used for the credit card detection. but it<s going to be useful when we will extend the DLP process with Names and Emails, etc.)

::

    python -m spacy download en_core_web_lg
    python -m spacy download fr_core_news_md


5. Test the installation

To test, run Python on the virtual env you've installed the presidio-analyzer in.
Then, make sure this code returns an answer:

.. code-block:: python
    :linenos:

    from dlp.analyzer_engine import AnalyzerEngine

    analyzer = AnalyzerEngine(enable_trace_pii=True)

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
