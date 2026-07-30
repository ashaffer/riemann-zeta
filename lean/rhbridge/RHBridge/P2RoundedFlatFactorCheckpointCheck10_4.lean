import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk4 :
    P2RoundedFactorCheckpointData.panel10FlatEven4 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel10FlatEven4_eq :
    P2RoundedFactorCheckpointData.panel10FlatEven4 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  exact panel10FlatComponentChunk4

end RHP2Bridge
