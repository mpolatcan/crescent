from pyformation import PyformationFactory as pf

pf.Template("").Resources(
    pf.ecr.Repository(id="EcrTest").LifecyclePolicy(
        pf.ecr.LifecyclePolicy()
    ).Tags(
        pf.Tag("test1", "test1"),
        pf.Tag("test2", "test2")
    )
).YAML("test")