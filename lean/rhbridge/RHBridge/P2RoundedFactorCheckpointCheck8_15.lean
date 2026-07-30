import RHBridge.P2RoundedFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FactorChunk15 :
    P2RoundedFactorCheckpointData.panel8Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨8, by decide⟩ := by
  decide +kernel

theorem panel8Prefix60_eq :
    P2RoundedFactorCheckpointData.panel8Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk15.1

theorem panel8Prefix61_eq :
    P2RoundedFactorCheckpointData.panel8Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk15.2.1

theorem panel8Prefix62_eq :
    P2RoundedFactorCheckpointData.panel8Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk15.2.2.1

theorem panel8Prefix63_eq :
    P2RoundedFactorCheckpointData.panel8Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk15.2.2.2

end RHP2Bridge
