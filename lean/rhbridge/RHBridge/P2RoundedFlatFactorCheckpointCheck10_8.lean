import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk8 :
    P2RoundedFactorCheckpointData.panel10FlatEven8 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel10FlatEven8_eq :
    P2RoundedFactorCheckpointData.panel10FlatEven8 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨8, by decide⟩ := by
  exact panel10FlatComponentChunk8

end RHP2Bridge
