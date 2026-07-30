import RHBridge.P2RoundedFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FactorChunk15 :
    P2RoundedFactorCheckpointData.panel30Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨30, by decide⟩ := by
  decide +kernel

theorem panel30Prefix60_eq :
    P2RoundedFactorCheckpointData.panel30Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk15.1

theorem panel30Prefix61_eq :
    P2RoundedFactorCheckpointData.panel30Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk15.2.1

theorem panel30Prefix62_eq :
    P2RoundedFactorCheckpointData.panel30Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk15.2.2.1

theorem panel30Prefix63_eq :
    P2RoundedFactorCheckpointData.panel30Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk15.2.2.2

end RHP2Bridge
