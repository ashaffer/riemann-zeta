import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel24FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel24FlatComponentChunk26

end RHP2Bridge
