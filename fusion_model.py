from tensorflow.keras import layers, models

def build_fusion_model(image_encoder,
                       tabular_input_dim,
                       num_classes):

    image_input = layers.Input(
        shape=(224,224,3)
    )

    tabular_input = layers.Input(
        shape=(tabular_input_dim,)
    )

    image_features = image_encoder(image_input)

    tabular_features = layers.Dense(
        64,
        activation='relu'
    )(tabular_input)

    fusion = layers.Concatenate()([
        image_features,
        tabular_features
    ])

    x = layers.Dense(
        128,
        activation='relu'
    )(fusion)

    x = layers.Dropout(0.4)(x)

    output = layers.Dense(
        num_classes,
        activation='softmax'
    )(x)

    model = models.Model(
        inputs=[image_input, tabular_input],
        outputs=output
    )

    return model