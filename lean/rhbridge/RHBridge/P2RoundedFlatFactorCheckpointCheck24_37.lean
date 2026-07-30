import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel24FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel24FlatComponentChunk37

end RHP2Bridge
