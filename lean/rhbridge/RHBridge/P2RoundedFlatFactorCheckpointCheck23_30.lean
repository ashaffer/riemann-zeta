import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel23FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel23FlatComponentChunk30

end RHP2Bridge
