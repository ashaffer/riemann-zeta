import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel24FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel24FlatComponentChunk43

end RHP2Bridge
