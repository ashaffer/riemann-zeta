import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel23FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel23FlatComponentChunk36

end RHP2Bridge
