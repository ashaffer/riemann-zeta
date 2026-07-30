import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk10 :
    P2RoundedFactorCheckpointData.panel27Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Prefix40_eq :
    P2RoundedFactorCheckpointData.panel27Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk10.1

theorem panel27Prefix41_eq :
    P2RoundedFactorCheckpointData.panel27Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk10.2.1

theorem panel27Prefix42_eq :
    P2RoundedFactorCheckpointData.panel27Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk10.2.2.1

theorem panel27Prefix43_eq :
    P2RoundedFactorCheckpointData.panel27Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk10.2.2.2

end RHP2Bridge
