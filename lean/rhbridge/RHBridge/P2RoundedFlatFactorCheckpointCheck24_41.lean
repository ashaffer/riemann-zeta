import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel24FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel24FlatComponentChunk41

end RHP2Bridge
