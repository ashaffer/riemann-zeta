import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel10FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel10FlatComponentChunk28

end RHP2Bridge
