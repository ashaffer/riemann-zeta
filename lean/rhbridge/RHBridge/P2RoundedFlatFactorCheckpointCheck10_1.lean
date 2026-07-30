import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk1 :
    P2RoundedFactorCheckpointData.panel10FlatEven1 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel10FlatEven1_eq :
    P2RoundedFactorCheckpointData.panel10FlatEven1 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  exact panel10FlatComponentChunk1

end RHP2Bridge
