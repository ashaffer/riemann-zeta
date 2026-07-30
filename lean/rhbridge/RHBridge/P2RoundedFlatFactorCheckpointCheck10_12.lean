import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk12 :
    P2RoundedFactorCheckpointData.panel10FlatEven12 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel10FlatEven12_eq :
    P2RoundedFactorCheckpointData.panel10FlatEven12 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  exact panel10FlatComponentChunk12

end RHP2Bridge
