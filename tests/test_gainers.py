from bin.gainers.factory import GainerFactory
from get_gainer import GainerPipeline

def test_mock_pipeline_runs():
    """Test that the mock processor pipeline runs without error"""
    processor = GainerFactory("mock").create_processor()
    pipeline = GainerPipeline(processor)
    pipeline.run()
