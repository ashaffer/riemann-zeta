import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk3 :
    P2RoundedFactorCheckpointData.panel27Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Prefix12_eq :
    P2RoundedFactorCheckpointData.panel27Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk3.1

theorem panel27Prefix13_eq :
    P2RoundedFactorCheckpointData.panel27Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk3.2.1

theorem panel27Prefix14_eq :
    P2RoundedFactorCheckpointData.panel27Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk3.2.2.1

theorem panel27Prefix15_eq :
    P2RoundedFactorCheckpointData.panel27Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk3.2.2.2

end RHP2Bridge
