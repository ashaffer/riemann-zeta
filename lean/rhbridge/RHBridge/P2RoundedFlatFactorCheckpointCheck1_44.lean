import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk44 :
    P2RoundedFactorCheckpointData.panel1FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd20_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨20, by decide⟩ := by
  exact panel1FlatComponentChunk44

end RHP2Bridge
