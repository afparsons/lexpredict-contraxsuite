# DocumentFieldCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type** | **str** |  | 
**code** | **str** | Field codes must be lowercase, should start with  a Latin letter, and contain only Latin letters, digits, underscores. Field codes must be unique to every Document Type. | 
**long_code** | **str** |  | [optional] [readonly] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**type** | **str** |  | 
**text_unit_type** | **str** |  | [optional] 
**value_detection_strategy** | **str** |  | [optional] 
**python_coded_field** | **str** |  | [optional] 
**classifier_init_script** | **str** | Classifier initialization script. Here is how it used: &lt;br /&gt;&lt;br /&gt;def&amp;nbsp;init_classifier_impl(field_code:&amp;nbsp;str,&amp;nbsp;init_script:&amp;nbsp;str):&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;if&amp;nbsp;init_script&amp;nbsp;is&amp;nbsp;not&amp;nbsp;None:&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;init_script&amp;nbsp;&#x3D;&amp;nbsp;init_script.strip()&lt;br /&gt;&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;if&amp;nbsp;not&amp;nbsp;init_script:&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;from&amp;nbsp;sklearn&amp;nbsp;import&amp;nbsp;tree&amp;nbsp;as&amp;nbsp;sklearn_tree&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;return&amp;nbsp;sklearn_tree.DecisionTreeClassifier()&lt;br /&gt;&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;from&amp;nbsp;sklearn&amp;nbsp;import&amp;nbsp;tree&amp;nbsp;as&amp;nbsp;sklearn_tree&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;from&amp;nbsp;sklearn&amp;nbsp;import&amp;nbsp;neural_network&amp;nbsp;as&amp;nbsp;sklearn_neural_network&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;from&amp;nbsp;sklearn&amp;nbsp;import&amp;nbsp;neighbors&amp;nbsp;as&amp;nbsp;sklearn_neighbors&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;from&amp;nbsp;sklearn&amp;nbsp;import&amp;nbsp;svm&amp;nbsp;as&amp;nbsp;sklearn_svm&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;from&amp;nbsp;sklearn&amp;nbsp;import&amp;nbsp;gaussian_process&amp;nbsp;as&amp;nbsp;sklearn_gaussian_process&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;from&amp;nbsp;sklearn.gaussian_process&amp;nbsp;import&amp;nbsp;kernels&amp;nbsp;as&amp;nbsp;sklearn_gaussian_process_kernels&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;from&amp;nbsp;sklearn&amp;nbsp;import&amp;nbsp;ensemble&amp;nbsp;as&amp;nbsp;sklearn_ensemble&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;from&amp;nbsp;sklearn&amp;nbsp;import&amp;nbsp;naive_bayes&amp;nbsp;as&amp;nbsp;sklearn_naive_bayes&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;from&amp;nbsp;sklearn&amp;nbsp;import&amp;nbsp;discriminant_analysis&amp;nbsp;as&amp;nbsp;sklearn_discriminant_analysis&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;from&amp;nbsp;sklearn&amp;nbsp;import&amp;nbsp;linear_model&amp;nbsp;as&amp;nbsp;sklearn_linear_model&lt;br /&gt;&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;eval_locals&amp;nbsp;&#x3D;&amp;nbsp;{&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&#39;sklearn_linear_model&#39;:&amp;nbsp;sklearn_linear_model,&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&#39;sklearn_tree&#39;:&amp;nbsp;sklearn_tree,&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&#39;sklearn_neural_network&#39;:&amp;nbsp;sklearn_neural_network,&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&#39;sklearn_neighbors&#39;:&amp;nbsp;sklearn_neighbors,&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&#39;sklearn_svm&#39;:&amp;nbsp;sklearn_svm,&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&#39;sklearn_gaussian_process&#39;:&amp;nbsp;sklearn_gaussian_process,&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&#39;sklearn_gaussian_process_kernels&#39;:&amp;nbsp;sklearn_gaussian_process_kernels,&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&#39;sklearn_ensemble&#39;:&amp;nbsp;sklearn_ensemble,&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&#39;sklearn_naive_bayes&#39;:&amp;nbsp;sklearn_naive_bayes,&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&#39;sklearn_discriminant_analysis&#39;:&amp;nbsp;sklearn_discriminant_analysis&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;}&lt;br /&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;return&amp;nbsp;eval_script(&#39;classifier&amp;nbsp;init&amp;nbsp;script&amp;nbsp;of&amp;nbsp;field&amp;nbsp;{0}&#39;.format(field_code),&amp;nbsp;init_script,&amp;nbsp;eval_locals)&lt;br /&gt; | [optional] 
**formula** | **str** |  | [optional] 
**convert_decimals_to_floats_in_formula_args** | **bool** | Floating point field values      are represented in Python Decimal type to avoid rounding problems in machine numbers representations.      Use this checkbox for converting them to Python float type before calculating the formula.      Float: 0.1 + 0.2 &#x3D; 0.30000000000000004. Decimal: 0.1 + 0.2 &#x3D; 0.3. | [optional] 
**value_regexp** | **str** | This regular expression is run on the sentence      found by a Field Detector and extracts a specific string value from a Text Unit. The first matching group is used if      the regular expression returns multiple matching groups. This is only applicable to string fields. | [optional] 
**depends_on_fields** | **list[str]** |  | [optional] 
**confidence** | **str** |  | [optional] 
**requires_text_annotations** | **bool** |  | [optional] 
**read_only** | **bool** |  | [optional] 
**category** | **int** |  | [optional] 
**family** | **int** |  | [optional] 
**default_value** | **object** | When populated, this      default value is displayed in the user interface’s annotator sidebar for the associated field. If not populated, the      Field Value remains empty by default. Please wrap entries with quotes, example: “landlord”. This is only applicable       to Choice and Multichoice fields. | [optional] 
**choices** | **str** | Newline-separated choices. A choice cannot contain a comma. | [optional] 
**allow_values_not_specified_in_choices** | **bool** |  | [optional] 
**stop_words** | **object** |  | [optional] 
**metadata** | **object** |  | [optional] 
**training_finished** | **bool** |  | [optional] 
**dirty** | **bool** |  | [optional] 
**order** | **int** |  | [optional] 
**trained_after_documents_number** | **int** |  | [optional] 
**hidden_always** | **bool** |  | [optional] 
**hide_until_python** | **str** |                      Enter a boolean expression in Python syntax. If this Python expression evaluates to True, then this              Document Field will be displayed in the user interface. Likewise, if this Python expression evaluates to              False, then this Document Field will be hidden from view. Importantly, if a document’s status is set to              complete and this Document Field remains hidden, then this Document Field’s data will be erased. Similarly,              this Document Field might contain data that a user can not review if it is hidden and the document has not              been set to complete. | [optional] 
**hide_until_js** | **str** | Target expression (\&quot;Hide until python\&quot; expression converted to JavaScript syntax for frontend). Allowed operators: +, -, *, /, &#x3D;&#x3D;&#x3D;, !&#x3D;&#x3D;, &#x3D;&#x3D;, !&#x3D;, &amp;&amp;, ||, &gt;, &lt;, &gt;&#x3D;, &lt;&#x3D;, % | [optional] [readonly] 
**display_yes_no** | **bool** | Checking this box will      display “Yes” if Related Info text is found, and display “No” if no text is found. | [optional] 
**detect_limit_unit** | **str** | Choose to add an upward limit to the amount of document text                                           ContraxSuite will search for this Document Field. For example, you can choose                                           to only search the first 10 paragraphs of text for the value required (this                                           often works best for values like “Company,” “Execution Date,” or “Parties,”                                          all of which typically appear in the first few paragraphs of a contract). | 
**detect_limit_count** | **int** | Specify the maximum  range for a bounded search. Field detection begins at the top of the document and continues until this Nth  \&quot;Detect limit unit\&quot; element. | 
**vectorizer_stop_words** | **str** | Stop words for vectorizers      user in field-based ML field detection. These stop words are excluded from going into the feature vector part      build based on this field. In addition to these words the standard sklearn \&quot;english\&quot; word list is used.      Format: each word on new line | [optional] 
**unsure_choice_value** | **str** | Makes sense for machine learning      strategies with \&quot;Unsure\&quot; category. The strategy will return this value if probabilities of all other categories      appear lower than the specified threshold. | [optional] 
**unsure_thresholds_by_value** | **object** | Makes sense for machine learning      strategies with \&quot;Unsure\&quot; category. The strategy will return concrete result (one of choice values) only if      the probability of the detected value is greater than this threshold. Otherwise the strategy returns None      or the choice value specified in \&quot;Unsure choice value\&quot; field. Format: { \&quot;value1\&quot;: 0.9, \&quot;value2\&quot;: 0.5, ...}.      Default: 0.9 | [optional] 
**mlflow_model_uri** | **str** | MLFlow model URI      understandable by the MLFlow artifact downloading routines. | [optional] 
**mlflow_detect_on_document_level** | **bool** | If true - whole      document text will be sent to the MLFlow model and the field value will be returned for the whole text with no     annotations. If false - each text unit will be sent separately. | [optional] 
**warning_message** | **str** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

