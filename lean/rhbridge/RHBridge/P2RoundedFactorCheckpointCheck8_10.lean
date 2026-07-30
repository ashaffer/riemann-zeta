import RHBridge.P2RoundedFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FactorChunk10 :
    P2RoundedFactorCheckpointData.panel8Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨8, by decide⟩ := by
  decide +kernel

theorem panel8Prefix40_eq :
    P2RoundedFactorCheckpointData.panel8Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk10.1

theorem panel8Prefix41_eq :
    P2RoundedFactorCheckpointData.panel8Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk10.2.1

theorem panel8Prefix42_eq :
    P2RoundedFactorCheckpointData.panel8Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk10.2.2.1

theorem panel8Prefix43_eq :
    P2RoundedFactorCheckpointData.panel8Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk10.2.2.2

end RHP2Bridge
