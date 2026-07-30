import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel1FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel1FlatComponentChunk46

end RHP2Bridge
