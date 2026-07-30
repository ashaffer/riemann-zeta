import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel23FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel23FlatComponentChunk43

end RHP2Bridge
