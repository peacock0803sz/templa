{
  description = "Templa";

  outputs = { ... }: {
    templates = {
      default.path = ./_common;
    };

  };
}
