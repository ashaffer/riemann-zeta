import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk16 :
    P2RoundedFactorCheckpointData.panel26FlatEven16 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel26FlatEven16_eq :
    P2RoundedFactorCheckpointData.panel26FlatEven16 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨16, by decide⟩ := by
  exact panel26FlatComponentChunk16

end RHP2Bridge
