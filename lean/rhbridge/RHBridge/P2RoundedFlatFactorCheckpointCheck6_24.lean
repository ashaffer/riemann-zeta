import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel6FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel6FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel6FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel6FlatComponentChunk24

end RHP2Bridge
