import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk2 :
    P2RoundedFactorCheckpointData.panel27Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Prefix8_eq :
    P2RoundedFactorCheckpointData.panel27Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk2.1

theorem panel27Prefix9_eq :
    P2RoundedFactorCheckpointData.panel27Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk2.2.1

theorem panel27Prefix10_eq :
    P2RoundedFactorCheckpointData.panel27Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk2.2.2.1

theorem panel27Prefix11_eq :
    P2RoundedFactorCheckpointData.panel27Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk2.2.2.2

end RHP2Bridge
