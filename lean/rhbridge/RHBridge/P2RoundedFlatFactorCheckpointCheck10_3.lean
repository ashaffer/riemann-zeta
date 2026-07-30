import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk3 :
    P2RoundedFactorCheckpointData.panel10FlatEven3 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel10FlatEven3_eq :
    P2RoundedFactorCheckpointData.panel10FlatEven3 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  exact panel10FlatComponentChunk3

end RHP2Bridge
