from d3m import index
from d3m.metadata.base import ArgumentType
from d3m.metadata.pipeline import Pipeline, PrimitiveStep


# Creating pipeline
pipeline_description = Pipeline()
pipeline_description.add_input(name='inputs')

# Step 0: dataset_to_dataframe
step_0 = PrimitiveStep(primitive=index.get_primitive('d3m.primitives.data_transformation.dataset_to_dataframe.Common'))
step_0.add_argument(name='inputs', argument_type=ArgumentType.CONTAINER, data_reference='inputs.0')
step_0.add_output('produce')
pipeline_description.add_step(step_0)


# Step 1: column_parser
step_1 = PrimitiveStep(primitive=index.get_primitive('d3m.primitives.data_transformation.column_parser.Common'))
step_1.add_argument(name='inputs', argument_type=ArgumentType.CONTAINER, data_reference='steps.0.produce')
step_1.add_output('produce')
pipeline_description.add_step(step_1)


# Step 2: HPFilter
step_2 = PrimitiveStep(primitive=index.get_primitive('d3m.primitives.tods.feature_analysis.hp_filter'))
step_2.add_argument(name='inputs', argument_type=ArgumentType.CONTAINER, data_reference='steps.1.produce')
step_2.add_output('produce')

step_2.add_hyperparameter(name = 'use_columns', argument_type=ArgumentType.VALUE, data = [2,3,6])

step_2.add_hyperparameter(name = 'use_semantic_types', argument_type=ArgumentType.VALUE, data = True)
step_2.add_hyperparameter(name = 'return_result', argument_type=ArgumentType.VALUE, data = 'append')
pipeline_description.add_step(step_2)

# Final Output
pipeline_description.add_output(name='output predictions', data_reference='steps.2.produce')

# Output to YAML
yaml = pipeline_description.to_yaml()
with open('pipeline.yml', 'w') as f:
    f.write(yaml)
print(yaml)

# Or you can output json
#data = pipline_description.to_json()

