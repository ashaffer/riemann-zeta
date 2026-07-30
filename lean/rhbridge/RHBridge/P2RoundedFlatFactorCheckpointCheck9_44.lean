import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk44 :
    P2RoundedFactorCheckpointData.panel9FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd20_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨20, by decide⟩ := by
  exact panel9FlatComponentChunk44

end RHP2Bridge
